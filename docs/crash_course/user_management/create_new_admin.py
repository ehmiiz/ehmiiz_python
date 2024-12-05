from admins import Admin

# Create an admin object
my_admin = Admin('Emil', 'Larsson', 'home/ehmiiz', '070707070', None)

# Display it's user and rights
my_admin.describe_user()
my_admin.privileges.add_privileges()
my_admin.privileges.show_privileges()