
import api from './api'
import React, {useState, useEffect} from 'react'


 function App() {
  //Declaration of value
  const [post, setPost] = useState([]);
  
  const [data, setData] = useState({
    notation: "", 
    resultat: ""
   });
  

  if (!post) return null;
//  Calcul for NPI in input
  const handleChange = (e) => {
    const value = e.target.value;
    setData({
      ...data,
      [e.target.name]: value
    });
  };
//  action Post in Fastapi for calcul 
  const handleSubmit = async (e) => {
    e.preventDefault();
    const userData = {
      notation: data.notation,
      resultat: "2"
    };
    await api.post("/calcul", userData).then((response) => {
      console.log(response.status, response.data.token);
    });
    fetchResultat();
  };
  // Get result after Calcul
  const fetchResultat = async () =>{
    const response = await api.get('/csvlast/');
    setPost(response.data)
  };


  return(
     
  <div>
    <nav className='navbar navbar-dark bg-primary'>
        <div className='container-fluid'>
          <a className='navbar-brand' href='#'>
            Calcul polonais
          </a>
        </div>

      </nav>
      <div class="container">
        <h2>Horizontal form</h2>
        <form class="form-horizontal" onSubmit={handleSubmit}>
          <div class="form-group">
            <label class="control-label col-sm-2" for="notation">Notation:</label>
            <div class="col-sm-10">
              <input type='text' name='notation' class="form-control" onChange={handleChange} value={data.notation}/>
            </div>
          </div>
          <div class="form-group">
            
            <div class="col-sm-6">          
                  <p >{post.notation}</p>
                  <p >{post.resultat}</p>
            </div>
          </div>
          <div class="form-group">        
            
          </div>
          <div class="form-group">        
            <div class="col-sm-offset-2 col-sm-10">
              <button type="submit" class="btn btn-default">Submit</button>
            </div>
          </div>
        </form>
      </div>
  </div>
    
  
  
        
  );
}
export default App;