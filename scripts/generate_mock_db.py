import os, sqlite3, random, time

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "mock", "aptos_logs.db")
os.makedirs(os.path.join(os.path.dirname(__file__), "..", "mock"), exist_ok=True)

random.seed(42)
now_s = int(time.time())
start_s = now_s - 60*45  # last 45 minutes

schema = """
DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  time INTEGER NOT NULL,
  timestamp_ms INTEGER NOT NULL,
  tool TEXT,
  grp TEXT,
  subcommand TEXT,
  network TEXT,
  profile TEXT,
  duration_ms INTEGER,
  exit_code INTEGER,
  args TEXT,
  stdout TEXT,
  stderr TEXT
);
"""

groups = [
  ("move","compile"),
  ("move","test"),
  ("move","publish"),
  ("account","fund-with-faucet"),
  ("account","create"),
  ("txs","submit"),
]
networks = ["devnet","testnet","mainnet"]
profiles = ["demo","default","ci"]
stdout_msgs = ["OK","Done","Published","Tests passed","Account created","Tx submitted"]
stderr_msgs = ["","network error","invalid profile","compile error","publish failed","rpc 429"]

def synth_event(t_s):
  grp, sub = random.choice(groups)
  net = random.choices(networks, weights=[6,3,1])[0]
  prof = random.choice(profiles)
  dur = int(random.gauss(1200 if grp=="move" else 400, 300))
  dur = max(80, abs(dur))
  base_fail = 0.04
  if grp=="move" and sub in ("publish","compile"): base_fail = 0.12
  fail = 1 if random.random() < base_fail else 0
  ec = 0 if fail==0 else random.choice([1,2,7])
  so = random.choice(stdout_msgs)
  se = "" if ec==0 else random.choice([m for m in stderr_msgs if m])
  args = f"--profile {prof} --network {net}"
  return {
    "time": t_s,
    "timestamp_ms": t_s * 1000 + random.randint(0,999),
    "tool": "aptos",
    "grp": grp,
    "sub": sub,
    "network": net,
    "profile": prof,
    "duration_ms": dur,
    "exit_code": ec,
    "args": args,
    "stdout": so,
    "stderr": se
  }

def main():
  conn = sqlite3.connect(DB_PATH)
  cur = conn.cursor()
  for stmt in schema.strip().split(";"):
    s = stmt.strip()
    if s:
      cur.execute(s + ";")

  rows = []
  t = start_s
  while t <= now_s:
    for _ in range(random.randint(4,10)):
      rows.append(synth_event(t + random.randint(0,59)))
    t += 60

  cur.executemany("""
    INSERT INTO logs (time,timestamp_ms,tool,grp,subcommand,network,profile,duration_ms,exit_code,args,stdout,stderr)
    VALUES (:time,:timestamp_ms,:tool,:grp,:sub,:network,:profile,:duration_ms,:exit_code,:args,:stdout,:stderr)
  """, rows)

  conn.commit()
  conn.close()
  print(f"Seeded {len(rows)} rows into {DB_PATH}")

if __name__ == "__main__":
  main()
