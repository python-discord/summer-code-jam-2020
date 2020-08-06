from django.test import TestCase

from .models import Board, Post, Comment


class BoardsTests(TestCase):
    def test_no_boards(self):
        """
        Tests if the 'boards' endpoint is responding and
        if the response initially contains no boards
        """
        resp = self.client.get('/nchan/boards/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 0)

    def test_returns_all_existing_boards(self):
        """
        Tests if 'boards' endpoint returns created boards
        """
        Board.objects.create(board='01', title='test-board-01')
        Board.objects.create(board='02', title='test-board-02')
        resp = self.client.get('/nchan/boards/')
        self.assertEqual(resp.data['count'], 2)
        self.assertEqual(resp.data['results'][0]['board'], '01')
        self.assertEqual(resp.data['results'][0]['title'], 'test-board-01')
        self.assertEqual(resp.data['results'][1]['board'], '02')
        self.assertEqual(resp.data['results'][1]['title'], 'test-board-02')

    def test_returns_single_board(self):
        """
        Tests if 'boards/<board>/' endpoint returns the correct board
        """
        Board.objects.create(board='01', title='test-board-01')
        Board.objects.create(board='02', title='test-board-02')
        resp1 = self.client.get('/nchan/boards/01/')
        self.assertEqual(resp1.data['board'], '01')
        self.assertEqual(resp1.data['title'], 'test-board-01')
        resp2 = self.client.get('/nchan/boards/02/')
        self.assertEqual(resp2.data['board'], '02')
        self.assertEqual(resp2.data['title'], 'test-board-02')

    def test_returns_board_posts(self):
        """
        Tests if 'boards/<board>/posts/' returns only
        that boards posts
        """
        Board.objects.create(board='01', title='test-board-01')
        Board.objects.create(board='02', title='test-board-02')
        Post.objects.create(title='first post', board=Board.objects.get(pk='01'), poster='festive-ferret',
                            text='Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        Post.objects.create(title='second post', board=Board.objects.get(pk='02'), poster='friendly-frogs',
                            text='sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')

        resp = self.client.get('/nchan/boards/01/posts/')
        self.assertEqual(resp.data['count'], 1)
        self.assertIn('first post', str(resp.data['results']))
        self.assertNotIn('second post', str(resp.data['results']))


class PostsTests(TestCase):
    def test_no_posts(self):
        """
        Tests if the 'posts' endpoint is responding and
        if the response initially contains no posts
        """
        resp = self.client.get('/nchan/posts/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['count'], 0)

    def test_returns_all_existing_posts(self):
        """
        Tests if 'posts' endpoint returns created posts
        """
        Board.objects.create(board='01', title='test-board-01')
        Post.objects.create(title='first post', board=Board.objects.get(pk='01'), poster='festive-ferret',
                            text='Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        Post.objects.create(title='second post', board=Board.objects.get(pk='01'), poster='friendly-frogs',
                            text='sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')

        resp = self.client.get('/nchan/posts/')
        self.assertEqual(resp.data['count'], 2)
        self.assertIn('first post', str(resp.data['results']))
        self.assertIn('second post', str(resp.data['results']))

    def test_returns_single_post(self):
        """
        Tests if 'posts/<id>/' endpoint returns the correct post
        """
        Board.objects.create(board='01', title='test-board-01')
        Post.objects.create(title='first post', board=Board.objects.get(pk='01'), poster='festive-ferret',
                            text='Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        resp = self.client.get('/nchan/posts/1/')
        self.assertEqual(resp.data['title'], 'first post')

    def test_returns_post_comments(self):
        """
        Tests if 'posts/<id>/comments/' endpoint returns correct comments
        """
        Board.objects.create(board='01', title='test-board-01')
        Post.objects.create(title='first post', board=Board.objects.get(pk='01'), poster='festive-ferret',
                            text='Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        Comment.objects.create(post=Post.objects.get(pk=1), commenter='glossy-gorillas',
                               text='URL namespace "admin" isn"t unique. You may not be'
                               'able to reverse all URLs in this namespace')
        resp = self.client.get('/nchan/posts/1/comments/')
        self.assertIn('glossy-gorillas', str(resp.data))


class CommentsTests(TestCase):
    def test_returns_comment(self):
        """
        Tests if 'comments/' endpoint returns comments
        """
        Board.objects.create(board='01', title='test-board-01')
        Post.objects.create(title='first post', board=Board.objects.get(pk='01'), poster='festive-ferret',
                            text='Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        Comment.objects.create(post=Post.objects.get(pk=1), commenter='glossy-gorillas',
                               text='URL namespace "admin" isn"t unique. You may'
                               'not be able to reverse all URLs in this namespace')
        resp = self.client.get('/nchan/comments/')
        self.assertIn('glossy-gorillas', str(resp.data))
