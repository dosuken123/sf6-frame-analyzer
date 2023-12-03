.PHONY: run
run:
	poetry run uvicorn sf6_frame_analyzer.main:app --reload