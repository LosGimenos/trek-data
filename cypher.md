//CREATE CONSTRAINT ON (d:Director) ASSERT d.name IS UNIQUE;
//CREATE CONSTRAINT ON (t:Teleplay) ASSERT t.name IS UNIQUE;
//CREATE CONSTRAINT ON (s:Story) ASSERT s.name IS UNIQUE;
//CREATE CONSTRAINT ON (c:Christian) ASSERT c.name IS UNIQUE;
//CREATE CONSTRAINT ON (i:IMDB) ASSERT i.name IS UNIQUE;

// Titles, Director, Story, Teleplay
USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///episodeDataSeasonOne.csv' AS line

CREATE (episode:Episode {name: line.Title, id: line.`Season & Episode` })

MERGE (christian:Christian {name: 'Christian' })
MERGE (director:Director {name: UPPER(line.`Directed by`) })
MERGE (teleplay:Teleplay {name: UPPER(line.`Teleplay by`) })
MERGE (story:Story {name: UPPER(line.`Story by`) })
MERGE (imdb:IMDB {name: 'IMDB' })
MERGE (imdbadj:IMDBadj {name: 'IMDB Adj' })
MERGE (jammer:Jammer {name: 'Jammer\'s' })
MERGE (jammeradj:Jammersadj {name: 'Jammer\'s Adj' })



CREATE (episode)-[:DIRECTOR]->(director)
CREATE (episode)-[:TELEPLAY]->(teleplay)
CREATE (episode)-[:STORY]->(story)
CREATE (christian)-[r:RATED]->(episode)
CREATE (imdb)-[i:RATED]->(episode)
CREATE (imdbadj)-[m:RATED]->(episode)
CREATE (jammer)-[j:RATED]->(episode)
CREATE (jammeradj)-[a:RATED]->(episode)

SET r.rating = line.Christian
SET i.rating = line.IMDB
SET m.rating = line.`IMDB Adj`
SET j.rating = line.`Jammer's`
SET a.rating = line.`Jammer's Adj`
