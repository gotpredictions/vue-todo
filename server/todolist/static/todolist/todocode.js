/**
 * 
 */
function startup() {
	
	$("#overlay").hide();
	
	thing.taskcreator = new Vue({
		el: "#addTask",
		data: {
			taskname: null
		}, 
		methods: {
			addTask: function(){
				name = this.taskname;
				$.post("/todo/create", JSON.stringify({name:this.taskname, is_done:false}), function(createStatus){
					createStatus = JSON.parse(createStatus);
					thing.taskdisplayer.tasklist.push({ id:createStatus.id, name:name, is_done: false});
				})
				.fail(function(response) {
				    alert('Error: ' + response.responseText);
				});

			}
		}
	})
	
	thing.taskdisplayer = new Vue({
		el: "#taskdisplay",
		data: {
			tasklist:[]
		},
		ready: function() {
			t = this.tasklist;
			$.get("/todo/list", function(listFromServer){
				listFromServer = JSON.parse(listFromServer);
				for( i = 0; i < listFromServer.length; i++){
					t.push({id:listFromServer[i][0], name:listFromServer[i][1], is_done:listFromServer[i][2]});
				}
			});
		},
		methods: {
			showOverlay: function(taskID){
				tid = taskID;
				$.get("/todo/details/"+taskID, function(taskDetails){
					taskDetails = JSON.parse(taskDetails);
					$("#overlay").dialog( "option", "title", taskDetails.name);
					thing.overlay.description = markdown.toHTML(taskDetails.description);
					thing.overlay.descriptiontxt = taskDetails.description;
					thing.overlay.tid = tid;
					thing.overlay.inEditMode = false;
					thing.overlay.waiting = false;
				})
				
				$("#overlay").dialog({
					modal:true
				});
			},
			unfinished: function(ID, status){
				for (i = 0;  i < this.tasklist.length; ++i){
					if(this.tasklist[i].id === ID){
						this.tasklist[i].is_done = status;
						$.post("/todo/update/"+ID, JSON.stringify({is_done:status}), function(data){})
						.fail(function(response) {
						    alert('Error: ' + response.responseText);
						});

					}
				}
			}
		}
	})
	
	thing.overlay = new Vue({
		el: "#description",
		data: {
			description: "",
			descriptiontxt: "",
			tid: "",
			inEditMode: false,
			waiting: false
		},
		methods: {
			edit: function(){
				this.inEditMode = true;
				console.log(tid);
			},
			save: function(){
				this.inEditMode = false;
				this.description = markdown.toHTML(this.descriptiontxt);
				this.waiting = true;
				$.post("/todo/update/"+this.tid, JSON.stringify({description:this.descriptiontxt}), function(data){
					thing.overlay.waiting = false;
				})
				.fail(function(response) {
				    alert('Error: ' + response.responseText);
				    thing.overlay.waiting = false;
				});

			}
			
		}
	})
	
}