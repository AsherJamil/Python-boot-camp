// app.js
document.addEventListener("DOMContentLoaded", () => {
	const columns = document.querySelectorAll(".task-list");
	const addTaskButtons = document.querySelectorAll(".add-task");

	// Initialize Sortable for each column
	columns.forEach((column) => {
		new Sortable(column, {
			group: "shared",
			animation: 150,
			ghostClass: "bg-gray-300",
		});
	});

	// Add task functionality
	addTaskButtons.forEach((button) => {
		button.addEventListener("click", () => {
			const taskContent = prompt("Enter task description:");
			if (taskContent) {
				const task = createTaskElement(taskContent);
				button.previousElementSibling.appendChild(task);
			}
		});
	});

	function createTaskElement(content) {
		const task = document.createElement("div");
		task.className = "bg-white p-2 mb-2 rounded shadow cursor-move";
		task.textContent = content;
		return task;
	}
});
