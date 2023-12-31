## Testing Workflow

- What's your input?
	- What will happen if any of the parameters:
		- Is Null
		- Is mismatch
			- Of different type
			- Of invalid type (length)
- What's you logic?
	- Can some other code modify your input?
	- Which other code waits for your output?
	- What will happen if you output null?
	- What will happen if your code doesn't provide its output on time?
	- Does your logic have all possible outputs defined?
	- Are all branches still relevant?
- Do you interact with data?
	- Do you CRUD Data?
		- What will happen if you lose rights to CRUD?
		- What will happen if the data is missing?
		- Can you distinguish between no access and no or corrupted data?
- Do you loop?
	- Are you always sure you'll always exit the loop?
	- Are you sure you need a loop?
	- Do you exit quickly on error?
	- Do you not enter the loop if it isn't necessary?
- Does the control flow runs smoothly or do you make unnecessary calls?

## References

Taken from [this tweet](https://twitter.com/hrisKoleva/status/1672903338898145280?s=20)