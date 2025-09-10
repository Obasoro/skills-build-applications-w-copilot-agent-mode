import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Fetched workouts:', results);
        console.log('Endpoint:', endpoint);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [endpoint]);

  return (
    <div className="card mb-4 shadow-sm">
      <div className="card-body">
        <h2 className="card-title text-danger mb-4">Workouts</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-danger">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Difficulty</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((workout, idx) => (
                <tr key={idx}>
                  <td>{idx + 1}</td>
                  <td>{workout.name}</td>
                  <td>{workout.difficulty}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
