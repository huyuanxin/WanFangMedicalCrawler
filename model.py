from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()


class Disease(Base):
    __tablename__ = 'disease'

    # id
    id = Column(Integer, primary_key=True)

    # 标准名
    standerName = Column(String(255))

    # 英文名
    englishName = Column(String(255))

    # 疾病编码
    diseaseCode = Column(String(255))

    # 描述
    describe = Column(String(1000))

    # 别名
    aliasName = Column(String(255))

    # 缩写名
    shortName = Column(String(255))

    # 分类
    type = Column(String(255))


class Drug(Base):
    __tablename__ = 'drug'

    # id
    id = Column(Integer, primary_key=True)

    # 标准名
    standerName = Column(String(255))

    # 英文名
    englishName = Column(String(255))

    # 别名
    aliasName = Column(String(255))

    # 描述
    describe = Column(String(1000))

    # 分类
    type = Column(String(255))


class Examination(Base):
    __tablename__ = 'examination'

    # id
    id = Column(Integer, primary_key=True)

    # 标准名
    standerName = Column(String(255))

    # 英文名
    englishName = Column(String(255))

    # 别名
    aliasName = Column(String(255))

    # 描述
    describe = Column(String(1000))

    # 分类
    type = Column(String(255))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/python')

Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)


# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
