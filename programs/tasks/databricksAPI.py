from databricks_api import DatabricksAPI


class DataBricksWorkspace:
    """
    A custom implemented API for databricks workspace
    """

    def __init__(self, host, user, password,):
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        """
        A method to connect databricks clustor
        :return:
        """
        try:
            db = DatabricksAPI(host=self.host, user=self.user, password=self.password)
            if db:
                return "Connection successfull"
            return "Can't connect"
        except Exception as err:
            pass

    def make_dir(self, path):
        """
        A method to create directory on databricks workspace
        :return:
        """
        response = DatabricksAPI.workspace.mkdirs(path, headers=None)
        if response:
            print("Directory created successfully")


# if __name__ == '__main__':
#     my_workspace = DataBricksWorkspace()
#     my_workspace.connect()
#     home = "path/to/dir/"
#     my_workspace.make_dir(path=home)


from databricks_api import DatabricksAPI


class AshishDataBricksWorkspace:

    def __init__(self):
        self.host = "https://dbc-7473fa97-a921.cloud.databricks.com/"
        self.user = "mihir.joshi@freestoneinfotech.com"
        self.password = "Welcome@123"
        self.db = None

    def connect(self):
        try:
            self.db = DatabricksAPI(host=self.host, user=self.user, password=self.password)
            if self.db:
                return "Connection successfull"
            return "Can't connect"
        except Exception as err:
            pass

    def make_dir(self, path):
        response = self.db.workspace.mkdirs(path, headers=None)
        if response:
            print("Directory created successfully")


if _name_ == '__main__':
    my_workspace = AshishDataBricksWorkspace()
    print(my_workspace.connect())

    home = "/Users/mihir.joshi@freestoneinfotech.com/as"
    my_workspace.make_dir(path=home)