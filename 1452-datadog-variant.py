'''
Datadog LC coding question

Description:
There iare a stream that has coming tags and also has a list of keywords, design a high performance filter to output thes keywords remaining tags. 
For example, a given stream: 
['apple, facebook, google', 
 'banana, facebook',
 'facebook, google, tesla',
 'intuit, google, facebook']

 If the keyword is ['apple'], the output should be ['facebook', 'google']
 If the keyword is ['facebook', 'google'], the output should be ['apple', 'tesla', 'intuit']

 The output can be in any order and can be put into a single list/array
'''

def filter_tags_by_keywords(stream, keywords):
    keyword_set = set(keywords)
    output_tags = set()

    for line in stream:
        tags = line.split(', ')
        tag_set = set(tags)

        if keyword_set.issubset(tag_set):
            output_tags.update(tag_set - keyword_set)
    
    return list(output_tags)

#test
stream = [
 'apple, facebook, google', 
 'banana, facebook',
 'facebook, google, tesla',
 'intuit, google, facebook'
]

keywords1 = ['apple']
keywords2 = ['facebook', 'google']
output1 = filter_tags_by_keywords(stream, keywords1)
output2 = filter_tags_by_keywords(stream, keywords2)
print(output1)
print(output2)