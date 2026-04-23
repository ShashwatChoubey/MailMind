up:
	docker compose up 
restart:
	docker compose up -d --build 
showcontainers: 
	docker ps 
logs:
	docker logs mailmind-backend-1
down:
	docker compose down  