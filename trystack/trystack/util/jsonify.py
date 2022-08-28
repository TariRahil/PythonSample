def jsonify(state={}, metadata={}, header={}, status =200):
	resource={}
	resource.update(state)
	resource.update(metadata)
	return resource, state, header
