from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
import grpc

from weather_pb2_grpc import WeatherGrpcServiceStub

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_PARAMS = {}
    DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, pool_pre_ping=True, **DATABASE_PARAMS)
engine_nullpool = create_async_engine(DATABASE_URL, **{"poolclass": NullPool})
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
async_session_taskmaker = async_sessionmaker(
    bind=engine_nullpool, expire_on_commit=False
)

channel = grpc.insecure_channel("10.1.179.64:50052")
grpc_client = WeatherGrpcServiceStub(channel)

class Base(DeclarativeBase):
    pass