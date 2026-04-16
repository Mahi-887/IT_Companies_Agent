import asyncio
import os
import uuid
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from app.core.config import get_settings
from app.models.db_models import RepositoryModel, DocumentModel

async def ingest():
    settings = get_settings()
    engine = create_async_engine(settings.database_url)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    async with async_session() as session:
        # Get the repo
        result = await session.execute(select(RepositoryModel).where(RepositoryModel.name == "devpulse-backend"))
        repo = result.scalar_one_or_none()
        if not repo:
            print("Repo not found. Run seed_db.py first.")
            return
            
        repo_id = repo.id
        
        # Scan local 'app' directory
        for root, dirs, files in os.walk("app"):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                    import hashlib
                    content_hash = hashlib.sha256(content.encode()).hexdigest()
                    
                    # Add to DB
                    doc = DocumentModel(
                        id=str(uuid.uuid4()),
                        repo_id=repo_id,
                        source_type="code",
                        title=file,
                        file_path=file_path,
                        content_hash=content_hash
                    )
                    session.add(doc)
                    print(f"Ingested: {file_path}")
        
        await session.commit()
        print("Ingestion complete.")

if __name__ == "__main__":
    asyncio.run(ingest())
