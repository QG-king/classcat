
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"comment": "用户信息表"}

    username: Mapped[str] = mapped_column(String(50), nullable=False, comment="账号")
    password: Mapped[str] = mapped_column(String(50), nullable=False, comment="密码")
    name: Mapped[str] = mapped_column(String(50), nullable=False, comment="名称")
    role:Mapped[str] = mapped_column(
        String(50),comment="角色:student-学生,admin-管理员",nullable=False
    )
    email: Mapped[str] = mapped_column(String(50), nullable=False, comment="邮箱")
    phone: Mapped[str] = mapped_column(String(50), nullable=False, comment="电话")
    avatar: Mapped[str] = mapped_column(String(50), nullable=False, comment="头像")
    status: Mapped[int] = mapped_column(nullable=False, comment="状态:0-禁用,1-正常")