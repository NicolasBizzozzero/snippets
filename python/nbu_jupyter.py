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

    
def plot_correlation_matrix(df, size=8, cmap="plasma", show=True):
    """ Plot a graphical correlation matrix for each pair of columns in the dataframe.
    
    :param df: pandas DataFrame.
    :param size: Vertical and horizontal size of the plot.
    """
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size + 1, size))
    img = ax.matshow(corr, cmap=cmap)
    fig.colorbar(img, ax=ax)
    ax.set_aspect('auto')
    plt.xticks(rotation=90)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)

    if show:
        plt.show()
