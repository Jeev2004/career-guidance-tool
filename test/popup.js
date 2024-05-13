document.getElementById('getHistory').addEventListener('click', () => {
    chrome.permissions.request({ permissions: ['history'] }, (granted) => {
      if (granted) {
        chrome.history.search({ text: '', maxResults: 100 }, (historyItems) => {
          // Process the historyItems data
          sendHistoryDataToDjango(historyItems);
        });
        
        chrome.history.search({ text: '', maxResults: 100 }, (historyItems) => {
          const historyList = document.getElementById('historyList');
          historyList.innerHTML = '';
  
          for (const item of historyItems) {
            const listItem = document.createElement('li');
            listItem.textContent = item.title || item.url;
            historyList.appendChild(listItem);
          }
        });
      } else {
        alert('Permission to access history denied.');
      }
    });
  });
  
  function sendHistoryDataToDjango(historyItems) {
    fetch('http://127.0.0.1:8000/api', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(historyItems),
    })
      .then((response) => response.json())
      .then((data) => {
        
        console.log('Data sent to Django:', data);
      })
      .catch((error) => {
        console.error('Error sending data to Django:', error);
      });
  }
  
  