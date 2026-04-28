import json

class ReflectionAgent:
    def __init__(self, tree_path):
        with open(tree_path, 'r') as f:
            self.tree = json.load(f)
        self.current_id = self.tree['start_node']
        self.state = {
            "answers": {},
            "signals": {
                "axis1": {"internal": 0, "external": 0},
                "axis2": {"contribution": 0, "entitlement": 0},
                "axis3": {"self": 0, "altro": 0}
            }
        }

    def interpolate(self, text):
        if not text: return ""
        # Replaces {node_id} with actual answers
        for node_id, ans in self.state["answers"].items():
            text = text.replace(f"{{{node_id}}}", str(ans))
        
        # Replaces axis dominants
        for axis in ["axis1", "axis2", "axis3"]:
            scores = self.state["signals"][axis]
            if sum(scores.values()) == 0:
                dominant = "neutral"
            else:
                dominant = max(scores, key=scores.get)
            text = text.replace(f"{{{axis}_dominant}}", dominant)
        return text

    def handle_decision(self, node):
        logic_string = node.get('logic', "")
        rules = logic_string.split(";")
        
        # Decision nodes usually look at the very last answer provided
        # In this tree, A1_D1 looks at A1_OPEN
        last_node_id = list(self.state["answers"].keys())[-1]
        last_answer = self.state["answers"].get(last_node_id)
        
        for rule in rules:
            if ":" not in rule: continue
            condition, target = rule.split(":")
            allowed_answers = condition.split("=")[1].split("|")
            if last_answer in allowed_answers:
                return target
        return "END"

    def run(self):
        while True:
            node = self.tree['nodes'].get(self.current_id)
            if not node:
                print("\n[SYSTEM]: Reflection Complete.")
                break

            # BUG FIX: If it's a decision node, skip printing and handle logic
            if node['type'] == 'decision':
                self.current_id = self.handle_decision(node)
                continue 

            # Interpolate text for displayable nodes
            display_text = self.interpolate(node.get('text', ""))

            if node['type'] in ['start', 'reflection', 'bridge', 'summary', 'end']:
                print(f"\n[AI]: {display_text}")
                if node['type'] == 'end': break
                input(">> Press Enter to continue...")
                self.current_id = node.get('target', 'END')

            elif node['type'] == 'question':
                print(f"\n[AI]: {display_text}")
                # Get options (can be list or dict)
                if isinstance(node['options'], dict):
                    opts = list(node['options'].keys())
                else:
                    opts = node['options']

                for i, o in enumerate(opts, 1):
                    print(f"  {i}. {o}")
                
                try:
                    choice = int(input(">> Select (1-{}): ".format(len(opts)))) - 1
                    selection = opts[choice]
                except (ValueError, IndexError):
                    print("Invalid selection. Try again.")
                    continue

                self.state["answers"][self.current_id] = selection

                # Process Signals
                if "signals" in node:
                    sig_key = node["signals"].get(selection)
                    if sig_key:
                        axis, pole = sig_key.split(":")
                        self.state["signals"][axis][pole] += 1

                # Move to next node
                if isinstance(node['options'], dict):
                    self.current_id = node['options'][selection]
                else:
                    # If it's a list, we assume there's a decision node coming up next
                    # We create the ID by adding _D1 as a convention
                    self.current_id = self.current_id + "_D1"

if __name__ == "__main__":
    agent = ReflectionAgent('tree/reflection_tree.json')
    agent.run()
