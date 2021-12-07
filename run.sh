cd client
npm run dev &
cd ../server
uvicorn app:app --reload --port 8002 &
