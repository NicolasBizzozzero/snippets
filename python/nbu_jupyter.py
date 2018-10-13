class PDF(object):
    """
        Create an iframe object with a specific pdf file embedded inside it.
        Thanks to Jakob for this class idea in this SO response :
        http://stackoverflow.com/questions/19470099/view-pdf-image-in-an-ipython-notebook/19470377#19470377

        Attributes :
            - path_to_pdf : str, the path locating the pdf file to load
            - size : tuple, the width and height (in pixels) of the iframe.
    """

    def __init__(self, path_to_pdf: str, size: tuple):
        self.path_to_pdf = path_to_pdf
        self.size = size

    def _repr_html_(self):
        """ Create and return the HTML code for the iframe and the pdf file
        inside it.
        """
        return ("<iframe src={0}"
                "        width={1[0]}"
                "        height={1[1]}>"
                "</iframe>").format(self.path_to_pdf, self.size)

    def _repr_latex_(self):
        """ Create and return the Latex code for the iframe and the pdf file
        inside it.
        """
        return r"\includegraphics[width=1.0\textwidth]{{{0}}}".format(self.path_to_pdf)

    
def plot_correlation_matrix(df, size=8, cmap="plasma", masked=False, show=True):
    """ Plot a graphical correlation matrix for each pair of columns in the dataframe.
    
    :param df: pandas DataFrame.
    :param size: Vertical and horizontal size of the plot.
    :param cmap: The ColorMap used to display the result. See : https://matplotlib.org/tutorials/colors/colormaps.html
    :param masked: Mask the upper diagonal of the heatmap.
    :param show: Show the result plotted.
    """
    corr = df.corr()
    
    if masked:
        corr[get_diagonal_mask(corr.values)] = np.nan
    
    fig, ax = plt.subplots(figsize=(size + 1, size))
    img = ax.matshow(corr, cmap=cmap)
    fig.colorbar(img, ax=ax)
    ax.set_aspect('auto')
    plt.xticks(rotation=90)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)

    if show:
        plt.show()


def get_diagonal_mask(data: np.ndarray) -> np.ndarray:
    """ Return a diagonal mask computed from an array.
    Useful when the data is the same if you transpose the array, eg in a heatmap.
    
    :param data: The np.ndarray from which you want to compute the mask.
    """
    mask = np.zeros_like(data, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    return mask
