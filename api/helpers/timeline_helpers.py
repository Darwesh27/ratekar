from timeline.models import *
from social.models import * 

def node_for_review(owner):
	privacy = PostPrivacy(level = 1)
	privacy.save()

	node = Node(owner = owner, kind = 3, privacy = privacy)
	node.save()

	return node

def create_parents(owner, kind, thought = None):


	# Cloning the default privacy settings
	privacy = owner.post_privacy

	if privacy == None:
		p = PostPrivacy()
		p.save()
		owner.post_privacy = p
		owner.save()

	privacy.pk = None
	privacy.save()

	post = Post(owner = owner, kind = kind , privacy = privacy)
	post.save()

	node = Node(owner = owner, kind = kind, privacy = privacy, post = post)
	node.save()

	thought = ThoughtDraft(text = thought, node = node)
	thought.save()


	return node


def fetch_user_posts(owner, viewer, kind = None, next = False, pid = None):

	raw_posts = []
	if viewer.is_friend_of(owner):
		raw_posts = owner.post_set.filter(privacy__level__in = [2,4,5]).order_by('-time').order_by('-id')
	elif owner == viewer: 
		raw_posts = owner.post_set.filter().order_by('-time').order_by('-id')
	else:
		raw_posts = owner.post_set.filter(privacy__level = 4).order_by('-time').order_by('-id')

	if len(raw_posts) > 0:
		if kind != None:
			raw_posts = raw_posts.filter(kind = kind)

		if pid != None:
			if next:
				raw_posts = raw_posts.filter(id__gt = pid)
			else:
				raw_posts = raw_posts.filter(id__lt = pid)

	if len(raw_posts) >= 5:
		raw_posts = raw_posts[0:5]

	return [post.node_set.all()[0].get_post(viewer) for post in raw_posts]











