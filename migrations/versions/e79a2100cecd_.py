"""empty message

Revision ID: e79a2100cecd
Revises: 
Create Date: 2019-03-10 20:08:07.293590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e79a2100cecd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('portfolios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_portfolios_name'), 'portfolios', ['name'], unique=False)
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('portfolio_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('company_sym', sa.String(length=256), nullable=True),
    sa.Column('website', sa.String(length=256), nullable=True),
    sa.Column('sector', sa.String(length=256), nullable=True),
    sa.Column('industry', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['portfolio_id'], ['portfolios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_company_sym'), 'company', ['company_sym'], unique=True)
    op.create_index(op.f('ix_company_industry'), 'company', ['industry'], unique=True)
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=True)
    op.create_index(op.f('ix_company_sector'), 'company', ['sector'], unique=True)
    op.create_index(op.f('ix_company_website'), 'company', ['website'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_company_website'), table_name='company')
    op.drop_index(op.f('ix_company_sector'), table_name='company')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_index(op.f('ix_company_industry'), table_name='company')
    op.drop_index(op.f('ix_company_company_sym'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_portfolios_name'), table_name='portfolios')
    op.drop_table('portfolios')
    op.drop_table('users')
    # ### end Alembic commands ###
