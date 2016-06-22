/**
 * 
 */
function startup() {
	
	var ID = 0;
	
	thing.taskcreator = new Vue({
		el: "#addTask",
		data: {
			taskname: null
		}, 
		methods: {
			addTask: function(){
				thing.taskdisplayer.tasklist.push({ id:ID, name:this.taskname, is_done: false});
				ID++;
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
			showOverlay: function(){
				$("#overlay").dialog({
					modal:true
				});
			}
		}
	})
}