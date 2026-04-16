from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_backend_scaffold_is_present() -> None:
    required_paths = [
        ROOT / "app" / "main.py",
        ROOT / "app" / "api" / "router.py",
        ROOT / "app" / "services" / "rag_query_service.py",
        ROOT / "migrations" / "001_initial_schema.sql",
    ]

    missing = [str(path) for path in required_paths if not path.exists()]
    assert not missing, f"Missing scaffold files: {missing}"


def test_api_contract_is_documented_in_code() -> None:
    main_file = (ROOT / "app" / "main.py").read_text(encoding="utf-8")
    assert "create_app" in main_file
    assert "api_router" in main_file
    assert "Modular monolith" in main_file

