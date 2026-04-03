class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def __repr__(self):
        return f'<Role name={self.name} permissions={self.permissions}>'

class User:
    def __init__(self, username, roles):
        self.username = username
        self.roles = roles  # List of Role objects

    def has_permission(self, action):
        return any(role.permissions.get(action, False) for role in self.roles)

    def __repr__(self):
        return f'<User username={self.username} roles={self.roles}>'


# Define roles with their permissions
super_admin = Role('SuperAdmin', {'create_user': True, 'manage_roles': True, 'view_audit_trails': True})

system_admin = Role('System Administrator', {'manage_users': True, 'view_reports': True})

production_manager = Role('Production Manager', {'view_production_metrics': True})

quality_inspector = Role('Quality Inspector', {'conduct_inspections': True})

assembly_supervisor = Role('Assembly Supervisor', {'assign_tasks': True})

inventory_manager = Role('Inventory Manager', {'manage_inventory': True})

finance = Role('Finance', {'view_financial_reports': True})

hr_manager = Role('HR Manager', {'manage_employee_records': True})

receiving_officer = Role('Receiving Officer', {'manage_receiving': True})

warehouse_controller = Role('Warehouse Controller', {'manage_warehouse': True})

supplier = Role('Supplier', {'view_products': True})

operator = Role('Operator', {'execute_production': True})


# Example Users
admin_user = User('admin', [super_admin, system_admin])
operator_user = User('operator1', [operator])

# Checking permissions
print(admin_user.has_permission('create_user'))  # True
print(operator_user.has_permission('create_user'))  # False

# Audit trails (this is placeholder logic)
audits = []

def log_audit(action, user):
    audits.append({'action': action, 'user': user.username, 'timestamp': '2026-04-03 08:49:58'})

log_audit('create_user', admin_user)  # Logging example

# Display audit records
for audit in audits:
    print(audit)