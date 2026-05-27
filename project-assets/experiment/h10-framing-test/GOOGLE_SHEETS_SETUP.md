# Google Sheets Data Collection Setup

## Step 1: Create Google Sheet

1. Go to sheets.google.com
2. Create new sheet named "H10 Framing Test Data"
3. Add headers in Row 1:
   - A: timestamp
   - B: prolificPID
   - C: condition
   - D: trust_1
   - E: trust_2
   - F: trust_3
   - G: trust_4
   - H: trust_5
   - I: trust_avg
   - J: attentionCheck
   - K: aiFamiliarity
   - L: age
   - M: gender
   - N: openEnded

## Step 2: Create Apps Script

1. In the sheet, go to Extensions → Apps Script
2. Delete default code, paste this:

```javascript
function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = JSON.parse(e.postData.contents);
    
    const trustAvg = (
      data.responses.trust_1 + 
      data.responses.trust_2 + 
      data.responses.trust_3 + 
      data.responses.trust_4 + 
      data.responses.trust_5
    ) / 5;
    
    sheet.appendRow([
      new Date().toISOString(),
      data.prolificPID,
      data.condition,
      data.responses.trust_1,
      data.responses.trust_2,
      data.responses.trust_3,
      data.responses.trust_4,
      data.responses.trust_5,
      trustAvg,
      data.attentionCheck,
      data.aiFamiliarity,
      data.demographics.age,
      data.demographics.gender,
      data.openEnded
    ]);
    
    return ContentService.createTextOutput(
      JSON.stringify({success: true})
    ).setMimeType(ContentService.MimeType.JSON);
    
  } catch (error) {
    return ContentService.createTextOutput(
      JSON.stringify({error: error.toString()})
    ).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput(
    "H10 Survey Backend is running"
  );
}
```

3. Save (Ctrl+S)
4. Deploy → New deployment
5. Type: Web app
6. Execute as: Me
7. Who has access: Anyone
8. Deploy → Copy the web app URL

## Step 3: Update Survey

Add the webhook URL to survey.html in the sendData function:

```javascript
function sendData(data) {
    const WEBHOOK_URL = 'YOUR_APPS_SCRIPT_URL_HERE';
    
    fetch(WEBHOOK_URL, {
        method: 'POST',
        body: JSON.stringify(data)
    }).catch(console.error);
    
    // Backup to localStorage
    const stored = JSON.parse(localStorage.getItem('h10_responses') || '[]');
    stored.push(data);
    localStorage.setItem('h10_responses', JSON.stringify(stored));
}
```

## Alternative: Manual Data Export

If you prefer not to set up Google Sheets:

1. Run the survey
2. Open browser DevTools (F12)
3. Console: `localStorage.getItem('h10_responses')`
4. Copy the JSON output
5. Paste into any JSON-to-CSV converter

---

*Both methods work. Google Sheets is automatic but needs setup. Manual export works immediately.*
