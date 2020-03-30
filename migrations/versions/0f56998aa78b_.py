"""empty message

Revision ID: 0f56998aa78b
Revises: 43e23db6cb4e
Create Date: 2020-03-29 14:17:28.943034

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0f56998aa78b'
down_revision = '43e23db6cb4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
                    sa.Column('post_id', sa.Integer(), nullable=True),
                    sa.Column('tag_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
                    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###