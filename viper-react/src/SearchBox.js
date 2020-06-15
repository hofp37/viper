import React from 'react';

const SearchBox = ({searchfield, searchChange}) => {
    return (
        <div className="tc pa2">
        <input
            className="pa3 ba b--black"
            type="search"
            placeholder="search models"
            onChange={searchChange}
        />
        </div>
    );
}

export default SearchBox;