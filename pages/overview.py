import pandas as pd
import os

def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    sessions_path = os.path.join(base_dir, "data", "wifi_sessions.csv")
    nodes_path = os.path.join(base_dir, "data", "wifi_nodes.csv")

    if not os.path.exists(sessions_path):
        sessions = pd.DataFrame({
            "session_id": [1, 2, 3],
            "user_count": [25, 40, 30],
            "duration": [15, 20, 10]
        })
    else:
        sessions = pd.read_csv(sessions_path)

    if not os.path.exists(nodes_path):
        nodes = pd.DataFrame({
            "node_id": [101, 102, 103],
            "location": ["A", "B", "C"]
        })
    else:
        nodes = pd.read_csv(nodes_path)

    return sessions, nodes
