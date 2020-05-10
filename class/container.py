class TagClouds:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagClouds()
cloud.add("PYTHON")
cloud.add("python")
cloud.add("Python")
cloud["java"] = 5
print(cloud["python"], cloud["java"])
print(len(cloud))
for tag in cloud:
    print(f"{tag}={cloud[tag]}")
print(cloud._TagClouds__tags)
