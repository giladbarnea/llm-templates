import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import Button
import numpy as np
import json

class InteractiveConceptMap:
    def __init__(self):
        # Create the concept map data structure
        self.data = {
            "nodes": [
                {"id": "framework", "label": "Hunch Generation Framework", "type": "main", "expanded": True},
                
                # Core Definition nodes
                {"id": "core_def", "label": "Core Definitions", "type": "section", "expanded": False},
                {"id": "attributes", "label": "Attributes", "type": "concept", "expanded": False, 
                 "details": "Measurable characteristics from event data"},
                {"id": "schema_attr", "label": "Schema-based", "type": "leaf", 
                 "details": "Direct from event properties (device_type, user_id)"},
                {"id": "calc_attr", "label": "Calculated", "type": "leaf", 
                 "details": "Computed from raw data (response time, session length)"},
                {"id": "llm_attr", "label": "LLM-derived", "type": "leaf", 
                 "details": "Extracted with language models (sentiment, topics)"},
                
                {"id": "hunch_types", "label": "Hunch Types", "type": "concept", "expanded": False,
                 "details": "Categories of hunches in the system"},
                {"id": "correlative", "label": "Correlative Hunch", "type": "leaf", 
                 "details": "Hypothesizes relationship between attribute and KPI"},
                {"id": "descriptive", "label": "Descriptive Hunch", "type": "leaf", 
                 "details": "Identifies patterns without claiming KPI impact"},
                
                # Hunch Structure nodes
                {"id": "structure", "label": "Hunch Structure", "type": "section", "expanded": False},
                {"id": "corr_structure", "label": "Correlative Structure", "type": "concept", "expanded": False,
                 "details": "Components of correlative hunches"},
                {"id": "desc_structure", "label": "Descriptive Structure", "type": "concept", "expanded": False,
                 "details": "Components of descriptive hunches"},
                
                {"id": "corr_components", "label": "Components", "type": "leaf", 
                 "details": "Identifier, Attribute, Hypothesis, Impact, Confidence"},
                {"id": "desc_components", "label": "Components", "type": "leaf", 
                 "details": "Identifier, Pattern, Prevalence, Trend, Segmentation"},
                
                # Implementation nodes
                {"id": "implementation", "label": "Implementation Workflow", "type": "section", "expanded": False},
                {"id": "initial_gen", "label": "1. Initial Generation", "type": "concept", "expanded": False,
                 "details": "First hunch creation from schema analysis"},
                {"id": "attr_extract", "label": "2. Attribute Extraction", "type": "concept", "expanded": False,
                 "details": "Processing events to extract attributes"},
                {"id": "testing", "label": "3. Testing & Validation", "type": "concept", "expanded": False,
                 "details": "Validating hunches against real data"},
                {"id": "discovery", "label": "4. New Hunch Discovery", "type": "concept", "expanded": False,
                 "details": "Ongoing discovery of new potential hunches"},
                {"id": "feedback", "label": "5. User Feedback", "type": "concept", "expanded": False,
                 "details": "Incorporating PM feedback for improvements"},
                
                # Example nodes
                {"id": "examples", "label": "Example Implementations", "type": "section", "expanded": False},
                {"id": "email_example", "label": "Email Draft Generation", "type": "concept", "expanded": False,
                 "details": "Hunches for email draft features"},
                {"id": "video_example", "label": "Video Recommendation", "type": "concept", "expanded": False,
                 "details": "Hunches for video recommendation features"}
            ],
            
            "edges": [
                # Core structure
                {"source": "framework", "target": "core_def"},
                {"source": "framework", "target": "structure"},
                {"source": "framework", "target": "implementation"},
                {"source": "framework", "target": "examples"},
                
                # Core definitions
                {"source": "core_def", "target": "attributes"},
                {"source": "core_def", "target": "hunch_types"},
                {"source": "attributes", "target": "schema_attr"},
                {"source": "attributes", "target": "calc_attr"},
                {"source": "attributes", "target": "llm_attr"},
                {"source": "hunch_types", "target": "correlative"},
                {"source": "hunch_types", "target": "descriptive"},
                
                # Structure section
                {"source": "structure", "target": "corr_structure"},
                {"source": "structure", "target": "desc_structure"},
                {"source": "corr_structure", "target": "corr_components"},
                {"source": "desc_structure", "target": "desc_components"},
                
                # Implementation section
                {"source": "implementation", "target": "initial_gen"},
                {"source": "implementation", "target": "attr_extract"},
                {"source": "implementation", "target": "testing"},
                {"source": "implementation", "target": "discovery"},
                {"source": "implementation", "target": "feedback"},
                
                # Examples section
                {"source": "examples", "target": "email_example"},
                {"source": "examples", "target": "video_example"},
                
                # Cross-connections
                {"source": "correlative", "target": "corr_structure", "type": "dotted"},
                {"source": "descriptive", "target": "desc_structure", "type": "dotted"}
            ]
        }
        
        # Additional details that can be shown when nodes are expanded
        self.expanded_details = {
            "email_example": [
                "Example Correlative Hunches:",
                "- iOS users accept drafts more than Android users",
                "- Emails with questions have higher acceptance rates",
                "- Positive sentiment drafts perform better",
                "- Formal language correlates with rejection",
                "",
                "Example Descriptive Hunches:",
                "- Most users discuss politics in emails",
                "- Users write emails outside business hours",
                "- Enterprise users use formal greetings"
            ],
            "video_example": [
                "Example Correlative Hunches:",
                "- Short videos have higher completion rates",
                "- Evening recommendations have higher acceptance",
                "- Mobile users prefer shorter videos",
                "- Educational content better on weekday mornings",
                "",
                "Example Descriptive Hunches:",
                "- Users consume content in 30-minute sessions",
                "- Weekend viewing favors entertainment content",
                "- Users alternate between multiple categories"
            ],
            "initial_gen": [
                "Process steps:",
                "1. Event Schema Analysis - examine available fields",
                "2. Generate Correlative Hunches (KPI impact)",
                "3. Generate Descriptive Hunches (patterns)",
                "4. Hunch Deduplication - filter duplicates"
            ],
            "attr_extract": [
                "Extraction methods:",
                "- Direct schema attributes (device_type, os)",
                "- Calculated attributes (timing, length)",
                "- LLM processing for text fields:",
                "  • Topics, sentiment, questions, formality",
                "  • Boolean flags, categories, scores"
            ],
            "testing": [
                "For Correlative Hunches:",
                "- Calculate KPI performance difference",
                "- Compute statistical significance (p-value)",
                "- Update impact and confidence scores",
                "- Apply minimum thresholds",
                "",
                "For Descriptive Hunches:",
                "- Calculate prevalence percentages",
                "- Track trends over time",
                "- Identify potential user segments"
            ],
            "corr_components": [
                "Correlative Hunch Components:",
                "1. Identifier: Unique ID for tracking",
                "2. Attribute: Characteristic being measured",
                "3. Hypothesis Statement: KPI impact prediction",
                "4. Extraction Workflow: Attribute derivation",
                "5. Current Impact: Measured KPI difference",
                "6. Confidence Score: Statistical significance",
                "7. Sample Size: Supporting event count",
                "8. Status: Active/Irrelevant/Archived"
            ],
            "desc_components": [
                "Descriptive Hunch Components:",
                "1. Identifier: Unique ID for tracking",
                "2. Pattern Statement: Behavioral observation",
                "3. Extraction Logic: Pattern identification",
                "4. Prevalence: % of users showing pattern",
                "5. Trend: Direction and rate of change",
                "6. Segmentation Potential: User segment definition",
                "7. Status: Active/Irrelevant/Archived"
            ],
            "discovery": [
                "New Hunch Discovery Process:",
                "1. Periodic generation of potential hunches",
                "2. Filtering against existing hunches",
                "3. Avoiding hunches marked as irrelevant",
                "4. Validating new hunches against data",
                "5. Adding significant findings to active hunches"
            ],
            "feedback": [
                "User Feedback Integration:",
                "1. PMs can mark hunches as:",
                "   - Valuable (prioritize similar patterns)",
                "   - Irrelevant (avoid similar patterns)",
                "   - Already Known (useful but not novel)",
                "2. Feedback guides future hunch generation",
                "3. Deprioritize categories marked irrelevant"
            ]
        }
        
        self.visible_nodes = {"framework"}
        self.visible_edges = []
        self.expanded_nodes = {"framework"}
        self.tooltip_visible = False
        self.tooltip_text = ""
        self.tooltip_pos = (0, 0)
        self.detail_boxes = {}
        
        # Create the figure and initial graph
        self.fig, self.ax = plt.subplots(figsize=(12, 10))
        plt.subplots_adjust(bottom=0.2)  # Make room for buttons
        self.create_buttons()
        self.update_graph()
        
        # Connect the click event
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_hover)
        
        plt.title("Interactive Hunch Generation Framework Concept Map")
        plt.show()
    
    def create_buttons(self):
        """Create control buttons for the visualization"""
        ax_expand = plt.axes([0.2, 0.05, 0.15, 0.05])
        ax_collapse = plt.axes([0.4, 0.05, 0.15, 0.05])
        ax_reset = plt.axes([0.6, 0.05, 0.15, 0.05])
        
        self.btn_expand = Button(ax_expand, 'Expand All')
        self.btn_collapse = Button(ax_collapse, 'Collapse All')
        self.btn_reset = Button(ax_reset, 'Reset View')
        
        self.btn_expand.on_clicked(self.expand_all)
        self.btn_collapse.on_clicked(self.collapse_all)
        self.btn_reset.on_clicked(self.reset_view)
    
    def update_graph(self):
        """Update the graph visualization based on visible nodes and edges"""
        self.ax.clear()
        
        # Create a new graph for the visible components
        G = nx.DiGraph()
        
        # Update visible edges based on visible nodes
        self.update_visible_edges()
        
        # Add nodes and edges to the graph
        node_colors = []
        node_sizes = []
        node_labels = {}
        edge_styles = []
        
        # Get all node objects by ID for easy lookup
        nodes_by_id = {node["id"]: node for node in self.data["nodes"]}
        
        # Add visible nodes to the graph
        for node_id in self.visible_nodes:
            node = nodes_by_id[node_id]
            G.add_node(node_id)
            
            # Set node appearance based on type
            if node["type"] == "main":
                node_colors.append('#6c5ce7')  # Purple for main concept
                node_sizes.append(1000)
            elif node["type"] == "section":
                node_colors.append('#74b9ff')  # Blue for sections
                node_sizes.append(800)
            elif node["type"] == "concept":
                node_colors.append('#81ecec')  # Teal for concepts
                node_sizes.append(600)
            else:  # leaf nodes
                node_colors.append('#e0f7fa')  # Light teal for leaf nodes
                node_sizes.append(500)
            
            node_labels[node_id] = node["label"]
        
        # Add visible edges to the graph
        for edge in self.visible_edges:
            source = edge["source"]
            target = edge["target"]
            G.add_edge(source, target)
            
            # Set edge appearance based on type
            if "type" in edge and edge["type"] == "dotted":
                edge_styles.append("dashed")
            else:
                edge_styles.append("solid")
        
        # Create the layout
        pos = nx.spring_layout(G, k=0.3, iterations=50, seed=42)
        
        # Draw the network
        nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.8, ax=self.ax)
        
        # Draw edges with different styles
        edges = list(G.edges())
        for i, (u, v) in enumerate(edges):
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=1.5, 
                                  style=edge_styles[i], alpha=0.7, 
                                  edge_color='gray', arrows=True, ax=self.ax)
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9, ax=self.ax)
        
        # Draw detail boxes for expanded nodes
        self.detail_boxes = {}
        for node_id in self.expanded_nodes:
            if node_id in self.expanded_details and node_id in pos:
                details = self.expanded_details[node_id]
                node_pos = pos[node_id]
                
                # Create a text box with the details
                text_box = self.ax.text(
                    node_pos[0] + 0.1, node_pos[1], 
                    '\n'.join(details),
                    bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.5'),
                    fontsize=8, ha='left', va='center'
                )
                self.detail_boxes[node_id] = text_box
        
        # Show tooltip if active
        if self.tooltip_visible:
            self.ax.text(
                self.tooltip_pos[0], self.tooltip_pos[1],
                self.tooltip_text,
                bbox=dict(facecolor='lightyellow', alpha=0.9, boxstyle='round,pad=0.5'),
                fontsize=8, ha='center', va='center'
            )
        
        # Remove axis and make it clean
        self.ax.axis('off')
        
        # Create a legend
        legend_elements = [
            mpatches.Patch(color='#6c5ce7', label='Main Concept'),
            mpatches.Patch(color='#74b9ff', label='Section'),
            mpatches.Patch(color='#81ecec', label='Concept'),
            mpatches.Patch(color='#e0f7fa', label='Detail')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right')
        
        self.fig.canvas.draw_idle()
        
    def update_visible_edges(self):
        """Update which edges should be visible based on visible nodes"""
        self.visible_edges = []
        for edge in self.data["edges"]:
            if edge["source"] in self.visible_nodes and edge["target"] in self.visible_nodes:
                self.visible_edges.append(edge)
    
    def get_children(self, node_id):
        """Get all children nodes of a given node"""
        children = []
        for edge in self.data["edges"]:
            if edge["source"] == node_id:
                children.append(edge["target"])
        return children
    
    def get_parent(self, node_id):
        """Get the parent node of a given node"""
        for edge in self.data["edges"]:
            if edge["target"] == node_id:
                return edge["source"]
        return None
    
    def toggle_node(self, node_id):
        """Toggle the expansion state of a node"""
        # Get all node objects by ID for easy lookup
        nodes_by_id = {node["id"]: node for node in self.data["nodes"]}
        node = nodes_by_id[node_id]
        
        children = self.get_children(node_id)
        
        # If node was collapsed, expand it
        if node_id not in self.expanded_nodes:
            self.expanded_nodes.add(node_id)
            # Add children to visible nodes
            for child_id in children:
                self.visible_nodes.add(child_id)
            node["expanded"] = True
        else:
            # If node was expanded, collapse it
            self.expanded_nodes.remove(node_id)
            
            # Remove all descendants from visible nodes
            descendants = set()
            to_process = children.copy()
            
            while to_process:
                current = to_process.pop()
                descendants.add(current)
                to_process.extend(self.get_children(current))
            
            # Also remove descendants from expanded nodes
            self.expanded_nodes -= descendants
            
            # Update visible nodes
            self.visible_nodes -= descendants
            node["expanded"] = False
        
        self.update_graph()
    
    def on_click(self, event):
        """Handle mouse click events"""
        if event.inaxes != self.ax:
            return
        
        # Check if a node was clicked
        for node_id in self.visible_nodes:
            # This is a simplified hit detection - in a real app you'd use the actual node positions
            # and check proper distances
            
            # Get all node objects by ID for easy lookup
            nodes_by_id = {node["id"]: node for node in self.data["nodes"]}
            
            # Here we would normally check if the click was inside a node
            # For this example, we'll simulate by checking if any visible node was clicked
            # (In a real implementation, we'd check coordinates against node positions)
            if event.xdata is not None and event.ydata is not None:
                # Check if a double-click occurred
                if event.dblclick:
                    # For demonstration, toggle the first node
                    self.toggle_node(node_id)
                    break
    
    def on_hover(self, event):
        """Handle mouse hover events"""
        if event.inaxes != self.ax:
            self.tooltip_visible = False
            self.update_graph()
            return
        
        # In a real implementation, we would check if mouse is over a node
        # and show its details as a tooltip
        # For this example, we're simulating this behavior
        
        # Check if hovering over a node (simplified)
        # (In a real implementation, we'd check coordinates against node positions)
        
        # Reset tooltip
        self.tooltip_visible = False
        
        # If mouse is over a node, show tooltip
        if event.xdata is not None and event.ydata is not None:
            # Update tooltip position
            self.tooltip_pos = (event.xdata, event.ydata)
            
            # Get all node objects by ID for easy lookup
            nodes_by_id = {node["id"]: node for node in self.data["nodes"]}
            
            # For demo purposes, only show tooltip for certain positions
            # In real app, check if mouse is over any node
            if 0.1 < event.xdata < 0.3 and 0.1 < event.ydata < 0.3:
                random_node = list(self.visible_nodes)[0]
                if "details" in nodes_by_id[random_node]:
                    self.tooltip_text = nodes_by_id[random_node]["details"]
                    self.tooltip_visible = True
        
        self.update_graph()
    
    def expand_all(self, event):
        """Expand all nodes in the graph"""
        # Get all node objects by ID for easy lookup
        nodes_by_id = {node["id"]: node for node in self.data["nodes"]}
        
        # Set all nodes as expanded
        for node in self.data["nodes"]:
            node["expanded"] = True
            self.expanded_nodes.add(node["id"])
            self.visible_nodes.add(node["id"])
        
        self.update_graph()
    
    def collapse_all(self, event):
        """Collapse all nodes except the root"""
        # Get all node objects by ID for easy lookup
        nodes_by_id = {node["id"]: node for node in self.data["nodes"]}
        
        # Collapse all nodes except the root
        self.expanded_nodes = {"framework"}
        self.visible_nodes = {"framework"}
        
        for node in self.data["nodes"]:
            if node["id"] != "framework":
                node["expanded"] = False
        
        # Add direct children of root to visible nodes
        for edge in self.data["edges"]:
            if edge["source"] == "framework":
                self.visible_nodes.add(edge["target"])
        
        self.update_graph()
    
    def reset_view(self, event):
        """Reset the view to the initial state"""
        # Reset to initial state
        self.visible_nodes = {"framework"}
        self.expanded_nodes = {"framework"}
        self.update_visible_edges()
        
        # Reset node expansion states
        for node in self.data["nodes"]:
            node["expanded"] = (node["id"] == "framework")
        
        # Add direct children of root to visible nodes
        for edge in self.data["edges"]:
            if edge["source"] == "framework":
                self.visible_nodes.add(edge["target"])
        
        self.update_graph()

# Run the application
if __name__ == "__main__":
    app = InteractiveConceptMap()