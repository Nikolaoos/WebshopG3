"""new migration

Revision ID: 3c4a47daab59
Revises: 
Create Date: 2022-02-09 23:11:21.030783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c4a47daab59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Categories',
    sa.Column('CategoryID', sa.Integer(), nullable=False),
    sa.Column('CategoryName', sa.String(length=80), nullable=False),
    sa.Column('Description', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('CategoryID')
    )
    op.create_table('Newsletters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('email_confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('password', sa.String(length=255), server_default='', nullable=False),
    sa.Column('first_name', sa.String(length=100), server_default='', nullable=False),
    sa.Column('last_name', sa.String(length=100), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Products',
    sa.Column('ProductID', sa.Integer(), nullable=False),
    sa.Column('ProductName', sa.String(length=40), nullable=False),
    sa.Column('SupplierID', sa.Integer(), nullable=False),
    sa.Column('CategoryId', sa.Integer(), nullable=False),
    sa.Column('QuantityPerUnit', sa.String(length=20), nullable=False),
    sa.Column('UnitPrice', sa.Float(), nullable=False),
    sa.Column('UnitsInStock', sa.Integer(), nullable=False),
    sa.Column('UnitsOnOrder', sa.Integer(), nullable=False),
    sa.Column('ReorderLevel', sa.Integer(), nullable=False),
    sa.Column('Discontinued', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['CategoryId'], ['Categories.CategoryID'], ),
    sa.PrimaryKeyConstraint('ProductID')
    )
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    op.drop_table('Products')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('Newsletters')
    op.drop_table('Categories')
    # ### end Alembic commands ###
