"""First revision

Revision ID: 6649d55dbbf0
Revises: 
Create Date: 2021-07-25 23:26:45.893343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6649d55dbbf0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subsidiary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subsidiary_id'), 'subsidiary', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dni', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_dni'), 'user', ['dni'], unique=True)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_hashed_password'), 'user', ['hashed_password'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('transmitter', sa.String(), nullable=False),
    sa.Column('receiver', sa.String(), nullable=False),
    sa.Column('from_subsidiary_id', sa.Integer(), nullable=True),
    sa.Column('to_subsidiary_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Numeric(), nullable=False),
    sa.Column('commission', sa.Numeric(), nullable=False),
    sa.Column('is_delivered', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['from_subsidiary_id'], ['subsidiary.id'], ),
    sa.ForeignKeyConstraint(['to_subsidiary_id'], ['subsidiary.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transaction_code'), 'transaction', ['code'], unique=True)
    op.create_index(op.f('ix_transaction_id'), 'transaction', ['id'], unique=False)
    op.create_index(op.f('ix_transaction_is_delivered'), 'transaction', ['is_delivered'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transaction_is_delivered'), table_name='transaction')
    op.drop_index(op.f('ix_transaction_id'), table_name='transaction')
    op.drop_index(op.f('ix_transaction_code'), table_name='transaction')
    op.drop_table('transaction')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_hashed_password'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_dni'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_subsidiary_id'), table_name='subsidiary')
    op.drop_table('subsidiary')
    # ### end Alembic commands ###
