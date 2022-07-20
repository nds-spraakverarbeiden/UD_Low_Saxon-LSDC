# remarks on the addenda

This directory is named as `not-to-release/` so that it will be ignored by the UD validation scripts. The content is to be integrated into the main corpus file. The additions in here are currently exclusively concerned with East Low German.

It uses a different ID system for sentences, in order to link sentences with their bibliographical references (`sources.txt`).

Annotation is done fully manually by means of spreadsheet software and a conversion to and from TSV. Note that spreadsheet software provides autocompletion, and for editing, we use the existing corpora as initial seed for autocompletion.

Middle Low German lemmas are only initially given. This is a lot of work :( For the moment, I focus on dialect coverage.

- For content words, MISC column contains either a comment on the source language, e.g. `(French)`, `(German)` or the MLG gloss according Lübben, Mnd. Handwörterbuch. Note that the coverage of Lübben isn't great.
- In Markian dialects, dative and accusative have collapsed into a single case ("in dat Hus"), all annotated as `Case=Acc`. However, there may be a differentiation in the dependencies: `obj` must have `Case=Acc`, but `Case=Acc` (without `case`) can also occur with `iobj` (roughly: if corresponding to a standard German dative) or `obl` (e.g., for temporal expressions: "ik bin *dissen Moandach* bi'n Noawer west")
- Much of modern Low German literacy is under strong influence from Standard German. Both in 19th c. and today, it can occur that Standard German syntax or Standard German inflections are used *in writing*, but they are actually not part of the vernacular. This pertains specifically to complex constructions with relative clauses and morphological inflection. This is particularly wide-spread in earlier literary texts. This was systematically used by Fritz Reuter, for example, and his "Germanized" way of writing is still considered as a role model. For historical texts, such interference with Standard German is not marked in the annotation, because for historical varieties (as all our data is), it is almost impossible to decide if a certain phenomenon is due to the genre (literary text with High German structures) or an actual feature of the dialect.
- Not all texts are literary, some have been created for the purpose of language documentation or ethnographic interest. These should have better quality. The difference is not marked either, because we sometimes don't know the ambitions and the intentions of the creator.