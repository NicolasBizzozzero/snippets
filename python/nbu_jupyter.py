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
