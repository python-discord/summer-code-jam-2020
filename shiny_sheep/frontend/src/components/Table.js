import React, {useEffect, useState, useCallback} from 'react';
import Checkbox from '@react95/core/Checkbox';



const Table = () =>{
    return (
        <div>
            <table className="table table-bordered">
                <thead className="thead-dark">
                    <tr>
                    <th scope="col">Channels</th>
                    <th scope="col">Groups</th>
                    <th scope="col">⭐/5</th>
                    <th scope="col">❤️</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th scope="row">#chess</th>
                    <td>42</td>
                    <td>4.5/5</td>
                    <td><input type="checkbox"></input></td>
                    </tr>
                    <tr>
                    <th scope="row">#gofish</th>
                    <td>2</td>
                    <td>3.5/5</td>
                    <td><input type="checkbox"></input></td>
                    </tr>
                    <tr>
                    <th scope="row">#poker</th>
                    <td>5</td>
                    <td>3.2</td>
                    <td><input type="checkbox"></input></td>
                    </tr>
                </tbody>
                </table>

                
            </div>
    );
}

export default Table;