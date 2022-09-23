from logging import raiseExceptions
import matplotlib.pylab as plt
import numpy as np

def CardinalPoly(nodes: list,i: int,t_list: list):
    """Helper function for InterpolerLangrangeForm.

    Args:
        nodes (list): x nodes
        i (int): index of the x node from which to develop
        t_list (list): Points of t where to evaluate

    Returns:
        list: List containing all the evaluated points for the given cardinal
    """
    assert type(nodes) == list, "Nodes are not a list"
    assert type(i) == int, "I is not of type int "
 
        
        
    node_i = nodes[i]
    nodes = nodes.copy()
    nodes.remove(node_i)
    np.asarray(nodes)
        
    li = lambda t: np.prod([((t-x)/(node_i-x)) for x in nodes])
    
    li_list = [li(t_element) for t_element in t_list]
    return li_list


def InterpolerLangrangeForm(nodes: list,y_list: list,t_list: list):
    """Interpolates a polynomia given a x and y values

    Args:
        nodes (list): Nodes of x values ordered of index i
        y_list (list): Corresponding y values of the x nodes
        t_list (list): list of points to evaluate the polynomia at

    Returns:
        lists: cardinals: solutions of the cardinals given the t_list, P_val: solution of the polynomia given t_list
    """
    assert len(y_list) == len(nodes), "list of x and y are not of equal length"
    P_val = []
    cardinals = []
    for idx in range(len(y_list)):
        cardinals.append(CardinalPoly(nodes,idx,t_list))
    np.asarray(cardinals)
    
    P_val = np.zeros(len(t_list))
    for idx,y in enumerate(y_list):
        P_val = np.add(P_val,np.multiply(cardinals[idx],y))
    
    return cardinals, P_val


def Lagrange_Plotter(nodes: list,y_list: list,t_list: list) -> object:
    """Plotter function for InterpolerLangrangeForm, to simplify the complete plotting

    Args:
        nodes (list): Nodes of x values ordered of index i
        y_list (list): Corresponding y values of the x nodes
        t_list (list): list of points to evaluate the polynomia at

    Returns:    
        object: Does not inherently return anything, but plots the descriped plot
    """
    assert type(nodes) == list, "Nodes are not a list"
    assert type(y_list) == list, "y_list are not a list"
    assert len(y_list) == len(nodes), "list of x and y are not of equal length"
    
    cardinal_solutions,polynomial_solution = InterpolerLangrangeForm(nodes,y_list,t_list)
    plt.plot(t_list,polynomial_solution)
    for solution in cardinal_solutions:
        plt.plot(t_list,solution)
    plt.scatter(nodes,y_list)
    plt.grid()
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.plot()