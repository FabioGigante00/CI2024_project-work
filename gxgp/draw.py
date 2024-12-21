#   *        Giovanni Squillero's GP Toolbox
#  / \       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2   +      A no-nonsense GP in pure Python
#    / \
#  10   11   Distributed under MIT License

import inspect

def draw(node: "Node", height: int):
    """ 
    Draws the tree of course. Note that if the depth is too high, you may need to save the output figure and then zoom in using a photo viewer.
    """
    import networkx as nx
    from networkx.drawing.nx_pydot import graphviz_layout
    import matplotlib.pyplot as plt
    import inspect

    if height < 0:
        raise ValueError(f"height can't be negative, but is {height}")
    
    if height == 0:
        plt.figure(figsize=(5,5))
        plt.scatter(0.5, 0.5, s=500, c='lightblue', marker='s')
        plt.text(0.5, 0.5, node.short_name, ha='center', va='center', fontsize=12)
        plt.axis('off')
        plt.show()
        return

    if height < 6:
        my_size = 30
    elif height == 6:
        my_size = 50
    elif height < 9:
        my_size = 100
    else:
        my_size = 200

    plt.figure(figsize=(my_size, my_size))

    # Create a mapping from nodes to integer IDs
    node_list = list(node.subtree)
    node_id_map = {n: idx for idx, n in enumerate(node_list)}

    G = nx.DiGraph()
    for n1 in node_list:
        for n2 in n1._successors:
            G.add_edge(node_id_map[n1], node_id_map[n2])

    # Use a layout algorithm
    try:
        pos = graphviz_layout(G, prog="dot")
    except:
        # Fallback to spring layout if graphviz_layout fails
        pos = nx.spring_layout(G)

    # Draw non-leaf nodes
    nx.draw_networkx_nodes(
        G,
        nodelist=[node_id_map[n] for n in node_list if not n.is_leaf],
        pos=pos,
        node_size=800,
        node_color='lightpink',
        node_shape='o'
    )

    # Draw leaf nodes with one keyword-only argument
    nx.draw_networkx_nodes(
        G,
        nodelist=[
            node_id_map[n] for n in node_list
            if n.is_leaf and len(inspect.getfullargspec(n._func).kwonlyargs) == 1
        ],
        pos=pos,
        node_size=500,
        node_color='lightgreen',
        node_shape='s'
    )

    # Draw leaf nodes with no keyword-only arguments
    nx.draw_networkx_nodes(
        G,
        nodelist=[
            node_id_map[n] for n in node_list
            if n.is_leaf and len(inspect.getfullargspec(n._func).kwonlyargs) == 0
        ],
        pos=pos,
        node_size=500,
        node_color='lightblue',
        node_shape='s'
    )

    # Draw labels
    nx.draw_networkx_labels(
        G,
        pos=pos,
        labels={node_id_map[n]: n.short_name for n in node_list},
    )

    # Draw edges
    nx.draw_networkx_edges(
        G,
        pos=pos
    )

    plt.show()
