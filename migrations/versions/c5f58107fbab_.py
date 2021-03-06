"""empty message

Revision ID: c5f58107fbab
Revises:
Create Date: 2021-01-02 23:28:13.120616

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c5f58107fbab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aislecontains')
    op.drop_table('aisles')
    op.drop_table('purchases')
    op.drop_table('providedby')
    op.drop_table('receivedfrom')
    op.drop_table('employees')
    op.drop_table('products')
    op.drop_table('departments')
    op.drop_table('providesdelivery')
    op.drop_table('customers')
    op.drop_table('suppliers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'suppliers',
        sa.Column(
            'id', sa.INTEGER(),
            server_default=sa.text("nextval('suppliers_id_seq'::regclass)"),
            autoincrement=True, nullable=False),
        sa.Column(
            'name', sa.VARCHAR(length=255),
            autoincrement=False, nullable=False),
        sa.Column(
            'address', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True),
        sa.Column(
            'phone', sa.VARCHAR(length=255),
            autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint('id', name='suppliers_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_table(
        'customers',
        sa.Column('id', sa.INTEGER(), server_default=sa.text(
            "nextval('customers_id_seq'::regclass)"),
            autoincrement=True, nullable=False),
        sa.Column(
            'name', sa.VARCHAR(length=255), autoincrement=False,
            nullable=True),
        sa.Column(
            'phone', sa.VARCHAR(length=255), autoincrement=False,
            nullable=True),
        sa.Column(
            'email', sa.VARCHAR(length=255), autoincrement=False,
            nullable=True),
        sa.PrimaryKeyConstraint('id', name='customers_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_table(
        'departments',
        sa.Column(
            'id', sa.INTEGER(),
            server_default=sa.text("nextval('departments_id_seq'::regclass)"),
            autoincrement=True, nullable=False),
        sa.Column(
            'name', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('id', name='departments_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_table(
        'products',
        sa.Column(
            'id', sa.INTEGER(),
            server_default=sa.text("nextval('products_id_seq'::regclass)"),
            autoincrement=True, nullable=False),
        sa.Column(
            'name', sa.VARCHAR(length=255),
            autoincrement=False, nullable=False),
        sa.Column(
            'price_per_cost_unit',
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False, nullable=False),
        sa.Column(
            'cost_unit', sa.VARCHAR(length=255),
            autoincrement=False, nullable=False),
        sa.Column(
            'department_id', sa.BIGINT(),
            autoincrement=False, nullable=False),
        sa.Column(
            'quantity_in_stock', sa.INTEGER(),
            autoincrement=False, nullable=True),
        sa.Column(
            'brand', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True),
        sa.Column(
            'production_date', sa.VARCHAR(length=10),
            autoincrement=False, nullable=True),
        sa.Column(
            'best_before_date', sa.VARCHAR(length=10),
            autoincrement=False, nullable=True),
        sa.Column(
            'plu', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column(
            'upc', sa.VARCHAR(length=20),
            autoincrement=False, nullable=True),
        sa.Column(
            'organic', sa.INTEGER(),
            autoincrement=False, nullable=True),
        sa.Column(
            'cut', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True),
        sa.Column(
            'animal', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ['department_id'], ['departments.id'],
            name='products_department_id_fkey'),
        sa.PrimaryKeyConstraint('id', name='products_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_table(
        'employees',
        sa.Column(
            'id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            'name', sa.VARCHAR(length=255),
            autoincrement=False, nullable=False),
        sa.Column(
            'department_id', sa.BIGINT(),
            autoincrement=False, nullable=True),
        sa.Column(
            'title', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True),
        sa.Column(
            'emp_number', sa.BIGINT(),
            autoincrement=False, nullable=False),
        sa.Column(
            'address', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True),
        sa.Column(
            'phone', sa.VARCHAR(length=255),
            autoincrement=False, nullable=True),
        sa.Column(
            'wage', sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column(
            'is_active', sa.BOOLEAN(), server_default=sa.text('true'),
            autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ['department_id'], ['departments.id'],
            name='employees_department_id_fkey'),
        sa.PrimaryKeyConstraint('id', name='employees_pkey')
    )
    op.create_table(
        'providesdelivery',
        sa.Column(
            'delivery_id', sa.INTEGER(),
            server_default=sa.text("nextval(\
                'providesdelivery_delivery_id_seq':: regclass)"),
            autoincrement=True, nullable=False),
        sa.Column(
            'supplier_id', sa.INTEGER(),
            autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ['supplier_id'], ['suppliers.id'],
            name='providesdelivery_supplier_id_fkey'),
        sa.PrimaryKeyConstraint('delivery_id', name='providesdelivery_pkey'),
        postgresql_ignore_search_path=False
    )
    op.create_table(
        'aisles',
        sa.Column(
            'aisle_number', sa.INTEGER(),
            autoincrement=False, nullable=False),
        sa.Column(
            'name', sa.VARCHAR(length=255),
            autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint(
            'aisle_number', name='aisles_pkey')
    )
    op.create_table(
        'aislecontains',
        sa.Column(
            'aisle_number', sa.INTEGER(),
            autoincrement=False, nullable=False),
        sa.Column(
            'product_id', sa.INTEGER(),
            autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ['aisle_number'], ['aisles.aisle_number'],
            name='aislecontains_aisle_number_fkey'),
        sa.ForeignKeyConstraint(
            ['product_id'], ['products.id'],
            name='aislecontains_product_id_fkey'),
        sa.PrimaryKeyConstraint(
            'aisle_number', 'product_id',
            name='aislecontains_pkey')
    )
    op.create_table(
        'purchases',
        sa.Column(
            'id', sa.INTEGER(),
            autoincrement=True, nullable=False),
        sa.Column(
            'product_id', sa.INTEGER(),
            autoincrement=False, nullable=False),
        sa.Column(
            'quantity', sa.INTEGER(),
            autoincrement=False, nullable=True),
        sa.Column(
            'customer_id', sa.INTEGER(),
            autoincrement=False, nullable=True),
        sa.Column(
            'purchase_date', sa.VARCHAR(length=10),
            autoincrement=False, nullable=True),
        sa.Column(
            'total', postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False, nullable=True),
        sa.Column(
            'is_cancelled', sa.BOOLEAN(),
            server_default=sa.text('false'),
            autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ['customer_id'], ['customers.id'],
            name='purchases_customer_id_fkey'),
        sa.ForeignKeyConstraint(
            ['product_id'], ['products.id'],
            name='purchases_product_id_fkey'),
        sa.PrimaryKeyConstraint('id', 'product_id', name='purchases_pkey')
    )
    op.create_table(
        'receivedfrom',
        sa.Column(
            'product_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            'delivery_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ['delivery_id'], ['providesdelivery.delivery_id'],
            name='receivedfrom_delivery_id_fkey'),
        sa.ForeignKeyConstraint(
            ['product_id'], ['products.id'],
            name='receivedfrom_product_id_fkey'),
        sa.PrimaryKeyConstraint(
            'product_id', 'delivery_id', name='receivedfrom_pkey')
    )
    op.create_table(
        'providedby',
        sa.Column(
            'product_id', sa.INTEGER(),
            autoincrement=False, nullable=False),
        sa.Column(
            'supplier_id', sa.INTEGER(),
            autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ['product_id'], ['products.id'],
            name='providedby_product_id_fkey'),
        sa.ForeignKeyConstraint(
            ['supplier_id'], ['suppliers.id'],
            name='providedby_supplier_id_fkey'),
        sa.PrimaryKeyConstraint(
            'supplier_id', 'product_id', name='providedby_pkey')
    )
    # ### end Alembic commands ###
