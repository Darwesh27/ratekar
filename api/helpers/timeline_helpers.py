from timeline.models import *
from social.models import * 

def create_parents(owner, kind, thought = None):


	# Cloning the default privacy settings
	privacy = owner.post_privacy
	privacy.pk = None
	privacy.save()

	post = Post(owner = owner, kind = kind , privacy = privacy)
	post.save()

	node = Node(owner = owner, kind = kind, privacy = privacy, post = post)
	node.save()

	thought = ThoughtDraft(text = thought, node = node)
	thought.save()


	return node
