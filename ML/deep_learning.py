def affine_forward(x, w, b):
    """
    Computes the forward pass for an affine (fully-connected) layer.

    The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
    examples, where each example x[i] has shape (d_1, ..., d_k). We will
    reshape each input into a vector of dimension D = d_1 * ... * d_k, and
    then transform it to an output vector of dimension M.

    Inputs:
    - x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
    - w: A numpy array of weights, of shape (D, M)
    - b: A numpy array of biases, of shape (M,)

    Returns a tuple of:
    - out: output, of shape (N, M)
    - cache: (x, w, b)
    """
    # out = None
    #MY CODE HERE:
    new_x = []
    for i in range(len(x)):
    	shape_x_i = np.shape(x[i])

    	reshaped_x_i = np.reshape(x[i], (np.prod(shape_x_i)))
    	new_x.append(reshaped_x_i)

    # print("AFFINE FORWARD FUNCTION")
    # print("X SHAPE:   ", np.shape(new_x))
    # print("W SHAPE:   ", np.shape(w))
    # print("B SHAPE:   ", np.shape(b))
    out = np.add(np.dot(new_x , w),  b)


    #############################################################################
    # TODO: Implement the affine forward pass. Store the result in out. You     #
    # will need to reshape the input into rows.                                 #
    #############################################################################
    # pass
    #############################################################################
    #                             END OF YOUR CODE                              #
    #############################################################################
    cache = (x, w, b)
    return out, cache


def affine_backward(dout, cache):
    """
    Computes the backward pass for an affine layer.

    Inputs:
    - dout: Upstream derivative, of shape (N, M)
    - cache: Tuple of:
      - x: Input data, of shape (N, d_1, ... d_k)
      - w: Weights, of shape (D, M)

    Returns a tuple of:
    - dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
    - dw: Gradient with respect to w, of shape (D, M)
    - db: Gradient with respect to b, of shape (M,)
    """

    # print("BELOW")
    #Xw + b 
    #average the gradient 
    
    x, w, b = cache

    # print("x shape", np.shape(x))
    # print("w shape", np.shape(w))
    # print("b shape", np.shape(b))
    # print("dout", np.shape(dout))
    # dx, dw, db = None, None, None
    
    x_transpose = x.T 
    # print("x transpose", np.shape(x_transpose))

    #must be same shape as dw. Always the same shape as what you are taking the derivative with respect to. 
    #how do you know? look up vector calculus...
    dx = np.reshape(np.matmul(dout, w.T), np.shape(x))

    #must be same shape as w.
    shape_x = np.shape(x)
    reshaped_x = np.reshape(x, (shape_x[0], np.prod(shape_x[1:])))
    # print(np.shape(reshaped_x))
    dw = np.matmul(dout.T, reshaped_x).T
    db = np.array([sum(i) for i in dout.T])

    # print("derivative shapes")
    # print("dx", np.shape(dx))
    # print("dw", np.shape(dw))
    # print("db", np.shape(db))

    #############################################################################
    # TODO: Implement the affine backward pass.                                 #
    #############################################################################
    # pass
    #############################################################################
    #                             END OF YOUR CODE                              #
    #############################################################################
    return dx, dw, db

def leaky_relu_forward(x):
    small_slope = 0.001
    out = np.where(x > 0, x, x*small_slope)



    cache = x, small_slope
    return out, cache

def leaky_relu_backward(dout, cache):
    x, small_slope = cache
    # print("shape of x", np.shape(x))
    # print("shape of dout", np.shape(dout))
    # dx = np.reshape(dout, (np.shape(x)))
    # print(x)
    ReLU_derivative = np.where(x > 0, x, small_slope)
    # print("shape of relu derivative", np.shape(ReLU_derivative))
    # print("ReLU derivative BELOW:   \n")
    # print(ReLU_derivative)
    dx = np.multiply(dout, ReLU_derivative)
    return dx 



def relu_forward(x):
    """
    Computes the forward pass for a layer of rectified linear units (ReLUs).

    Input:
    - x: Inputs, of any shape

    Returns a tuple of:
    - out: Output, of the same shape as x
    - cache: x
    """
    out = np.maximum(x, 0)
    #############################################################################
    # TODO: Implement the ReLU forward pass.                                    #
    #############################################################################
    # pass
    #############################################################################
    #                             END OF YOUR CODE                              #
    #############################################################################
    cache = x
    return out, cache


def relu_backward(dout, cache):
    """
    Computes the backward pass for a layer of rectified linear units (ReLUs).

    Input:
    - dout: Upstream derivatives, of any shape
    - cache: Input x, of same shape as dout

    Returns:
    - dx: Gradient with respect to x
    """
    # dx, x = None, cache
    x = cache
    # print("shape of x", np.shape(x))
    # print("shape of dout", np.shape(dout))
    # dx = np.reshape(dout, (np.shape(x)))
    # print(x)
    ReLU_derivative = np.heaviside(x, 0)
    # print("shape of relu derivative", np.shape(ReLU_derivative))
    # print("ReLU derivative BELOW:   \n")
    # print(ReLU_derivative)
    dx = np.multiply(dout, ReLU_derivative)

    #############################################################################
    # TODO: Implement the ReLU backward pass.                                   #
    #############################################################################
    # pass
    #############################################################################
    #                             END OF YOUR CODE                              #
    #############################################################################
    return dx
