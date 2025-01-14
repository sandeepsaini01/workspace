"""Update models with correct table names and relationships

Revision ID: 17b04f999994
Revises: c0bd15b95a27
Create Date: 2024-09-05 15:02:46.511281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '17b04f999994'
down_revision: Union[str, None] = 'c0bd15b95a27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('magazines', 'id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('magazines', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('magazines', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_index(op.f('ix_magazines_id'), 'magazines', ['id'], unique=False)
    op.create_index(op.f('ix_magazines_name'), 'magazines', ['name'], unique=True)
    op.alter_column('plans', 'id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('plans', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('plans', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_index(op.f('ix_plans_id'), 'plans', ['id'], unique=False)
    op.create_index(op.f('ix_plans_title'), 'plans', ['title'], unique=True)
    op.drop_constraint('plans_magazine_id_fkey', 'plans', type_='foreignkey')
    op.drop_column('plans', 'magazine_id')
    op.alter_column('subscriptions', 'id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('subscriptions', 'user_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('subscriptions', 'magazine_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('subscriptions', 'plan_id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('subscriptions', 'renewal_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
    op.alter_column('subscriptions', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.create_index(op.f('ix_subscriptions_id'), 'subscriptions', ['id'], unique=False)
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.alter_column('users', 'id',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)
    op.drop_column('users', 'is_active')
    op.drop_column('users', 'email')
    op.drop_index(op.f('ix_subscriptions_id'), table_name='subscriptions')
    op.alter_column('subscriptions', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('subscriptions', 'renewal_date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    op.alter_column('subscriptions', 'plan_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.alter_column('subscriptions', 'magazine_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.alter_column('subscriptions', 'user_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.alter_column('subscriptions', 'id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)
    op.add_column('plans', sa.Column('magazine_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key('plans_magazine_id_fkey', 'plans', 'magazines', ['magazine_id'], ['id'])
    op.drop_index(op.f('ix_plans_title'), table_name='plans')
    op.drop_index(op.f('ix_plans_id'), table_name='plans')
    op.alter_column('plans', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('plans', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('plans', 'id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)
    op.drop_index(op.f('ix_magazines_name'), table_name='magazines')
    op.drop_index(op.f('ix_magazines_id'), table_name='magazines')
    op.alter_column('magazines', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('magazines', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('magazines', 'id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
