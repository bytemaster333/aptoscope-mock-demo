.PHONY: seed up down clean reset

seed:
	python3 scripts/generate_mock_db.py

up:
	docker compose up -d

down:
	docker compose down

clean:
	rm -f mock/aptos_logs.db

reset: down
	rm -f mock/aptos_logs.db
	$(MAKE) seed
	$(MAKE) up
