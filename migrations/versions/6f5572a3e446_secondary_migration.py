"""Secondary migration

Revision ID: 6f5572a3e446
Revises: 
Create Date: 2024-05-17 19:44:19.028542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f5572a3e446'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('about_me',
               existing_type=sa.VARCHAR(length=140),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('about_me',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=140),
               existing_nullable=True)

    # ### end Alembic commands ###
