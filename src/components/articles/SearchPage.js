// components/SearchPage.js
import React, { useState } from 'react';
import styles from './SearchPage.css';

function SearchPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [author, setAuthor] = useState('');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async (event) => {
    event.preventDefault();
    if (!searchTerm && !author && !category && !date) {
      alert('Please fill at least one field to start the search.');
      return;
    }

    const queryParts = [];
    if (searchTerm) queryParts.push(`all:${encodeURIComponent(searchTerm)}`);
    if (author) queryParts.push(`au:${encodeURIComponent(author)}`);
    if (category) queryParts.push(`cat:${encodeURIComponent(category)}`);
    if (date) {
      queryParts.push(`submittedDate:[${date}T00:00:00Z+TO+${date}T23:59:59Z]`);
    }

    const queryString = queryParts.join('+AND+');
    const apiUrl = `http://export.arxiv.org/api/query?search_query=${queryString}&start=0&max_results=10`;

    try {
      const response = await fetch(apiUrl);
      const text = await response.text();
      const parser = new DOMParser();
      const xml = parser.parseFromString(text, "application/xml");
      parseResults(xml);
    } catch (error) {
      console.error('Error fetching data: ', error);
      setResults([]);
    }
  };

  const parseResults = (xml) => {
    const entries = xml.getElementsByTagName('entry');
    const newResults = Array.from(entries).map(entry => ({
      title: entry.getElementsByTagName('title')[0].textContent,
      summary: entry.getElementsByTagName('summary')[0].textContent.trim(),
      published: entry.getElementsByTagName('published')[0].textContent.substring(0, 10),
      id: entry.getElementsByTagName('id')[0].textContent,
      authors: Array.from(entry.getElementsByTagName('author')).map(author => author.getElementsByTagName('name')[0].textContent).join(', '),
      categories: Array.from(entry.getElementsByTagName('category')).map(cat => cat.getAttribute('term')).join(', ')
    }));
    setResults(newResults);
  };

return (
        <div className={styles.container}>
            <h1>Search for Articles</h1>
            <form onSubmit={handleSearch} className={styles.form}>
                <input type="text" className={styles.input} placeholder="Enter search terms, e.g., 'quantum physics'" value={searchTerm} onChange={e => setSearchTerm(e.target.value)} />
                <span>                                                       </span>
                <input type="text" className={styles.input} placeholder="Author, e.g., 'Einstein'" value={author} onChange={e => setAuthor(e.target.value)} />
                <span>                                                       </span>
                <input type="text" className={styles.input} placeholder="Category, e.g., 'physics:cond-mat'" value={category} onChange={e => setCategory(e.target.value)} />
                <span>                                                       </span>
                <input type="date" className={styles.input} value={date} onChange={e => setDate(e.target.value)} />
                <span>                                                       </span>
                <button type="submit" className={styles.button}>Search</button>
            </form>
            {results.length > 0 && (
                <div className={styles.results}>
                    {results.map((result, index) => (
                        <div key={index} className={styles.resultItem}>
                            <h3>{result.title}</h3>
                            <p>Authors: {result.authors}</p>
                            <p>{result.summary}</p>
                            <p>Published on: {result.published}</p>
                            <p>Categories: {result.categories}</p>
                            <p><a href={result.id} target="_blank" rel="noopener noreferrer">Read Full Text</a></p>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default SearchPage;
