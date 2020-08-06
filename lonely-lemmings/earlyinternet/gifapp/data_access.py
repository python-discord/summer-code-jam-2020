class UserDA:
    def retrieve_by_pk(self, pk):
        pass
    # retrieve
    # insert
    # update
    # delete


class ProjectDA:
    # retrieve
    def retrieve_by_pk(self, pk):
        pass

    def retrieve_by_user_id(self, pk):
        pass

    # insert
    # update
    # delete
    def delete_by_pk(self, pk):
        pass


class ImageDA:
    # retrieve
    def retrieve_by_pk(self, pk):
        pass

    def retrieve_by_project_id(self, project_id):
        pass

    def retrieve_by_user_id(self, user_id):
        pass

    # insert
    def insert_by_project_id(self, project_id):
        pass
    # update
    # delete
    pass


class CommentDA:
    # retrieve
    def retrieve_by_pk(self, pk):
        pass

    def retrieve_by_project_id(self, project_id):
        pass

    def retrieve_by_parent_id(self, parent_id):
        pass

    # insert
    def insert_by_parent_id(self, parent_id):
        pass

    def insert_by_project_id(self, parent_id):
        pass

    # update
    # delete
