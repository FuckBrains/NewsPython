from spinrewriterapi import SpinRewriterAPI
from gingerit.gingerit import GingerIt

import language_tool_python
tool = language_tool_python.LanguageTool('en-US')  # use a local server (automatically set up), language English

# your Spin Rewriter email address goes here
email_address = "monk0062006@gmail.com"

# your unique Spin Rewriter API key goes here
api_key = "0db159e#42c4a65_d1e1aee?54a19a9"

# Spin Rewriter API settings - authentication:
spinrewriter_api = SpinRewriterAPI(email_address, api_key)

#
# (optional) Set a list of protected terms.
# You can use one of the following formats:
# - protected terms are separated by the '\n' (newline) character
# - protected terms are separated by commas (comma-separated list)
# - protected terms are stored in a Python [] array
#
protected_terms = "John, Douglas Adams, then"
#protected_terms = "John\nDouglas\nAdams\nthen"
#protected_terms = ["John", "Douglas", "Adams", "then"]

spinrewriter_api.set_protected_terms(protected_terms)

# (optional) Set whether the One-Click Rewrite process automatically protects
# Capitalized Words outside the article's title.
spinrewriter_api.set_auto_protected_terms(False)

# (optional) Set the confidence level of the One-Click Rewrite process.
spinrewriter_api.set_confidence_level("medium")

# (optional) Set whether the One-Click Rewrite process uses nested spinning syntax (multi-level spinning) or not.
spinrewriter_api.set_nested_spintax(True)

# (optional) Set whether Spin Rewriter rewrites complete sentences on its own.
spinrewriter_api.set_auto_sentences(False)

# (optional) Set whether Spin Rewriter rewrites entire paragraphs on its own.
spinrewriter_api.set_auto_paragraphs(False)

# (optional) Set whether Spin Rewriter writes additional paragraphs on its own.
spinrewriter_api.set_auto_new_paragraphs(False)

# (optional) Set whether Spin Rewriter changes the entire structure of phrases and sentences.
spinrewriter_api.set_auto_sentence_trees(False)

# (optional) Sets whether Spin Rewriter should only use synonyms (where available) when generating spun text.
spinrewriter_api.set_use_only_synonyms(False)

# (optional) Sets whether Spin Rewriter should intelligently randomize the order of paragraphs and lists when
# generating spun text.
spinrewriter_api.set_reorder_paragraphs(False)

# (optional) Sets whether Spin Rewriter should automatically enrich generated articles with headings, bulpoints, etc.
spinrewriter_api.set_add_html_markup(False)

# (optional) Sets whether Spin Rewriter should automatically convert line-breaks to HTML tags.
spinrewriter_api.set_use_html_linebreaks(False)

# Make the actual API request and save the response as a native JSON object.
text = "A sentence with a error in the Hitchhiker’s Guide to the Galaxy."
# Make the actual API request and save the response as a native JSON dictionary or False on error
result = spinrewriter_api.get_unique_variation(text)

parser = GingerIt()
response = result.get("response")

res = parser.parse(text)
lt = tool.correct(text)


#output = parser.parse(result.get("response"))
print("--------------------------------------------")
print(res)
print("--------------------------------------------")
print(lt)
if result:
    print("Spin Rewriter API response")
    #print(result)
else:
    print("Spin Rewriter API error")



