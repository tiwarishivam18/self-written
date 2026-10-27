def validate_server(server: dict) -> bool:
    """
    Validates a single server dictionary based on a set of rules.

    Rules:
    - Must be a dictionary.
    - Must contain 'name', 'region', and 'status' keys.
    - 'name' and 'region' must be non-empty strings.
    - 'status' must be either 'active' or 'inactive'.

    Args:
        server: A dictionary representing a server.

    Returns:
        True if the server is valid, False otherwise.
    """
    # TODO: Implement the validation logic for a single server.
    # 1. Check if the input is a dictionary.
    # 2. Check for the presence of all required keys.
    # 3. Check the data types and values for 'name', 'region', and 'status'.
    # Return False at the first sign of invalid data.


    keys_needed = ['name', 'region', 'status']

    if not isinstance(server, dict):
        return False
            
    elif not all(k in server for k in keys_needed):
        return False



    if (
        not isinstance(server['name'], str)
        or not server['name'].strip()
        or not isinstance(server['region'], str)
        or not server['region'].strip()
        or server['status'] not in ['active', 'inactive']
    ):
        return False

    return True

def generate_inventory_report(servers: list[dict]) -> dict:
    """
    Processes a list of server dictionaries to generate a structured inventory report,
    ignoring any invalid server entries.

    Args:
        servers: A list of dictionaries, where each dictionary represents a server.

    Returns:
        A dictionary where keys are regions, containing 'active' and 'inactive' lists.
    """
    # TODO: Implement the report generation logic.
    # 1. Handle non-list inputs gracefully.
    # 2. Initialize an empty dictionary for the report.
    # 3. Loop through the 'servers' list. For each server...
    # 4. ...call validate_server(). If it's invalid, skip to the next server.
    # 5. If it's valid, extract its data and add it to the report, creating new region entries as needed.
    # 6. Return the final report.

    if not isinstance(servers, list):
        return {}

    valid_servers = [server for server in servers if validate_server(server)]

    report = {}

    for server in valid_servers:
        if server['region'] not in report:
            report[server['region']] = {'active': [], 'inactive': []}
            if server['status'] == 'active':
                report[server['region']]['active'].append(server['name'])
            elif server['status'] == 'inactive':
                report[server['region']]['inactive'].append(server['name'])


        elif server['status'] == 'active':
            report[server['region']]['active'].append(server['name'])
        elif server['status'] == 'inactive':
            report[server['region']]['inactive'].append(server['name'])


    return report