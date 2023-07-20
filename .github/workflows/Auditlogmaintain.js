const { Octokit } = require('@octokit/rest');
const fs = require('fs');

// Replace 'YOUR_GITHUB_ACCESS_TOKEN' with your actual GitHub personal access token.
const octokit = new Octokit({ auth: 'YOUR_GITHUB_ACCESS_TOKEN' });

// Replace 'your-username' and 'your-repo' with the GitHub repository details.
const owner = 'your-username';
const repo = 'your-repo';

// File path where the audit logs will be stored.
const logFilePath = './audit-logs.txt';

// Function to write the log data to the file.
function writeLogToFile(logData) {
  fs.appendFile(logFilePath, logData + '\n', (err) => {
    if (err) {
      console.error('Error writing to the log file:', err);
    }
  });
}

// Fetch audit logs for the repository.
async function fetchAuditLogs() {
  try {
    const response = await octokit.repos.listCommits({
      owner,
      repo,
    });

    // Process each commit and write the log data to the file.
    response.data.forEach((commit) => {
      const { sha, commit: commitInfo, author } = commit;
      const logData = `SHA: ${sha} | Author: ${author.login} | Date: ${commitInfo.author.date} | Message: ${commitInfo.message}`;
      writeLogToFile(logData);
    });

    console.log('Audit logs generated successfully.');
  } catch (err) {
    console.error('Error fetching audit logs:', err);
  }
}
