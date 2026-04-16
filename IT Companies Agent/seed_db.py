import asyncio
import uuid
import jwt
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings
from app.models.db_models import Base, RepositoryModel
from app.models.entities import Repository

async def seed():
    settings = get_settings()
    engine = create_async_engine(settings.database_url)
    
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    async with async_session() as session:
        # Check if repo exists
        from sqlalchemy import select
        result = await session.execute(select(RepositoryModel).where(RepositoryModel.name == "devpulse-backend"))
        if result.scalar_one_or_none():
            print("Database already seeded.")
        else:
            repo_id = str(uuid.uuid4())
            user_id = "user_123"
            
            repo = RepositoryModel(
                id=repo_id,
                owner_user_id=user_id,
                name="devpulse-backend",
                github_url="https://github.com/example/devpulse-backend",
                default_branch="main"
            )
            session.add(repo)
            await session.commit()
            print(f"Created repository: {repo_id}")
            
        # Generate JWT for user_123
        from app.core.security import generate_token
        token = generate_token("user_123", "dev@example.com")
        print("\n" + "="*50)
        print("COPY THIS TOKEN FOR THE FRONTEND (sessionStorage.setItem('token', '...'))")
        print("="*50)
        print(token)
        print("="*50 + "\n")

if __name__ == "__main__":
    asyncio.run(seed())
