"""empty message

Revision ID: b2dfd563bc8a
Revises: 
Create Date: 2019-05-18 16:33:24.449385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2dfd563bc8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('social_id', sa.String(length=64), nullable=True),
    sa.Column('social_username', sa.String(length=64), nullable=True),
    sa.Column('social_email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('social_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_social_email'), 'users', ['social_email'], unique=False)
    op.create_index(op.f('ix_users_social_username'), 'users', ['social_username'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gen_image_path', sa.String(length=250), nullable=True),
    sa.Column('gen_image_width', sa.Integer(), nullable=True),
    sa.Column('gen_image_height', sa.Integer(), nullable=True),
    sa.Column('num_iters', sa.Integer(), nullable=True),
    sa.Column('model_name', sa.String(length=120), nullable=True),
    sa.Column('total_loss', sa.String(length=120), nullable=True),
    sa.Column('style_loss', sa.String(length=120), nullable=True),
    sa.Column('content_loss', sa.String(length=120), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_name'), 'tasks', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tasks_name'), table_name='tasks')
    op.drop_table('tasks')
    op.drop_table('images')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_social_username'), table_name='users')
    op.drop_index(op.f('ix_users_social_email'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
